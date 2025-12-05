from flask import Flask, render_template, jsonify
import requests
import time
from collections import Counter, defaultdict
import math

app = Flask(__name__)

API_BASE = "https://draw.ar-lottery01.com"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Origin': 'https://dkwin9.com',
    'Referer': 'https://dkwin9.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site'
}

NUMBER_TO_COLOR = {
    0: ['Red', 'Violet'],
    1: ['Green'],
    2: ['Red'],
    3: ['Green'],
    4: ['Red'],
    5: ['Green', 'Violet'],
    6: ['Red'],
    7: ['Green'],
    8: ['Red'],
    9: ['Green']
}

def get_color_list(color_string):
    colors = []
    if 'green' in color_string.lower():
        colors.append('Green')
    if 'red' in color_string.lower():
        colors.append('Red')
    if 'violet' in color_string.lower():
        colors.append('Violet')
    return colors if colors else ['Unknown']

def get_big_small(number):
    return 'Big' if int(number) >= 5 else 'Small'

def get_number_color(number):
    return NUMBER_TO_COLOR.get(int(number), ['Unknown'])


class PredictionEngine:
    def __init__(self, history):
        self.history = history
        self.numbers = [int(h['number']) for h in history if h.get('number', '') != '']
        self.big_small_list = [h['big_small'] for h in history if h.get('big_small')]
        
    def analyze_frequency(self, window=50):
        if len(self.numbers) < 5:
            return {i: 0.1 for i in range(10)}
        
        recent = self.numbers[:min(window, len(self.numbers))]
        counts = Counter(recent)
        total = len(recent)
        
        freq = {}
        for i in range(10):
            freq[i] = counts.get(i, 0) / total if total > 0 else 0.1
        return freq
    
    def analyze_hot_cold(self, hot_window=10, cold_window=50):
        if len(self.numbers) < hot_window:
            return {i: 0.5 for i in range(10)}
        
        hot_counts = Counter(self.numbers[:hot_window])
        cold_counts = Counter(self.numbers[:min(cold_window, len(self.numbers))])
        
        scores = {}
        for i in range(10):
            hot_freq = hot_counts.get(i, 0) / hot_window
            cold_freq = cold_counts.get(i, 0) / min(cold_window, len(self.numbers))
            
            if hot_freq > cold_freq * 1.5:
                scores[i] = 0.7
            elif hot_freq < cold_freq * 0.5:
                scores[i] = 0.6
            else:
                scores[i] = 0.5
        return scores
    
    def analyze_streaks(self):
        if len(self.big_small_list) < 3:
            return {'predicted': None, 'strength': 0}
        
        streak_count = 1
        streak_value = self.big_small_list[0]
        
        for i in range(1, min(10, len(self.big_small_list))):
            if self.big_small_list[i] == streak_value:
                streak_count += 1
            else:
                break
        
        if streak_count >= 4:
            return {
                'predicted': 'Small' if streak_value == 'Big' else 'Big',
                'strength': min(0.85, 0.6 + streak_count * 0.05)
            }
        elif streak_count >= 3:
            return {
                'predicted': 'Small' if streak_value == 'Big' else 'Big',
                'strength': 0.7
            }
        
        return {'predicted': None, 'strength': 0}
    
    def analyze_transitions(self):
        if len(self.numbers) < 10:
            return {i: {j: 0.1 for j in range(10)} for i in range(10)}
        
        transitions = defaultdict(lambda: defaultdict(int))
        for i in range(len(self.numbers) - 1):
            prev_number = self.numbers[i + 1]
            curr_number = self.numbers[i]
            transitions[prev_number][curr_number] += 1
        
        trans_prob = {}
        for i in range(10):
            total = sum(transitions[i].values())
            trans_prob[i] = {}
            for j in range(10):
                trans_prob[i][j] = transitions[i][j] / total if total > 0 else 0.1
        
        return trans_prob
    
    def analyze_alternating_pattern(self):
        if len(self.big_small_list) < 6:
            return {'is_alternating': False, 'next': None, 'strength': 0}
        
        recent = self.big_small_list[:6]
        alternating_count = 0
        for i in range(len(recent) - 1):
            if recent[i] != recent[i + 1]:
                alternating_count += 1
        
        if alternating_count >= 4:
            next_val = 'Small' if recent[0] == 'Big' else 'Big'
            return {
                'is_alternating': True,
                'next': next_val,
                'strength': 0.65 + (alternating_count - 4) * 0.05
            }
        
        return {'is_alternating': False, 'next': None, 'strength': 0}
    
    def analyze_color_patterns(self):
        if len(self.history) < 10:
            return {'Green': 0.5, 'Red': 0.5, 'Violet': 0.2, 'streak': None}
        
        color_counts = {'Green': 0, 'Red': 0, 'Violet': 0}
        total = 0
        
        for h in self.history[:50]:
            colors = h.get('colors', [])
            for c in colors:
                if c in color_counts:
                    color_counts[c] += 1
            total += 1
        
        recent_primary_colors = []
        for h in self.history[:10]:
            colors = h.get('colors', [])
            if colors:
                primary = 'Green' if 'Green' in colors else 'Red'
                recent_primary_colors.append(primary)
        
        color_streak = None
        if len(recent_primary_colors) >= 4:
            if all(c == 'Green' for c in recent_primary_colors[:4]):
                color_streak = 'Red'
            elif all(c == 'Red' for c in recent_primary_colors[:4]):
                color_streak = 'Green'
        
        freqs = {k: v / total if total > 0 else 0.33 for k, v in color_counts.items()}
        return {
            'frequencies': freqs,
            'streak': color_streak
        }
    
    def analyze_gap_pattern(self):
        if len(self.numbers) < 20:
            return {i: 0 for i in range(10)}
        
        last_seen = {}
        for idx, num in enumerate(self.numbers):
            if num not in last_seen:
                last_seen[num] = idx
        
        gap_scores = {}
        for i in range(10):
            gap = last_seen.get(i, 20)
            if gap >= 15:
                gap_scores[i] = 0.8
            elif gap >= 10:
                gap_scores[i] = 0.7
            elif gap >= 7:
                gap_scores[i] = 0.6
            else:
                gap_scores[i] = 0.3
        
        return gap_scores
    
    def calculate_number_probabilities(self):
        if len(self.numbers) < 5:
            return {i: 0.1 for i in range(10)}
        
        freq_scores = self.analyze_frequency()
        hot_cold_scores = self.analyze_hot_cold()
        gap_scores = self.analyze_gap_pattern()
        trans_probs = self.analyze_transitions()
        
        last_number = self.numbers[0] if self.numbers else 0
        trans_scores = trans_probs.get(last_number, {i: 0.1 for i in range(10)})
        
        combined = {}
        for i in range(10):
            score = (
                freq_scores.get(i, 0.1) * 0.15 +
                hot_cold_scores.get(i, 0.5) * 0.25 +
                gap_scores.get(i, 0.5) * 0.35 +
                trans_scores.get(i, 0.1) * 0.25
            )
            combined[i] = score
        
        total = sum(combined.values())
        if total > 0:
            combined = {k: v / total for k, v in combined.items()}
        
        return combined
    
    def predict(self):
        if len(self.numbers) < 5:
            import random
            num = random.randint(0, 9)
            return {
                'number': num,
                'big_small': get_big_small(num),
                'colors': get_number_color(num),
                'confidence': 50,
                'analysis': {
                    'method': 'random',
                    'reason': 'Insufficient data for analysis'
                }
            }
        
        streak_analysis = self.analyze_streaks()
        alternating_analysis = self.analyze_alternating_pattern()
        color_analysis = self.analyze_color_patterns()
        number_probs = self.calculate_number_probabilities()
        
        predicted_big_small = None
        big_small_confidence = 0
        analysis_method = []
        preferred_color = None
        
        if color_analysis['streak']:
            preferred_color = color_analysis['streak']
            analysis_method.append(f"Color streak detected - expect {preferred_color}")
        
        if streak_analysis['strength'] > 0.6:
            predicted_big_small = streak_analysis['predicted']
            big_small_confidence = streak_analysis['strength']
            analysis_method.append(f"Streak reversal detected")
        
        if alternating_analysis['is_alternating'] and alternating_analysis['strength'] > big_small_confidence:
            predicted_big_small = alternating_analysis['next']
            big_small_confidence = alternating_analysis['strength']
            analysis_method.append(f"Alternating pattern detected")
        
        if predicted_big_small is None:
            big_count = self.big_small_list[:20].count('Big')
            small_count = self.big_small_list[:20].count('Small')
            
            if big_count > small_count + 2:
                predicted_big_small = 'Small'
                big_small_confidence = 0.6
                analysis_method.append("Big/Small imbalance - expect Small")
            elif small_count > big_count + 2:
                predicted_big_small = 'Big'
                big_small_confidence = 0.6
                analysis_method.append("Big/Small imbalance - expect Big")
            else:
                predicted_big_small = 'Small' if big_count >= small_count else 'Big'
                big_small_confidence = 0.55
                analysis_method.append("Statistical balance prediction")
        
        if predicted_big_small == 'Big':
            filtered_probs = {k: v for k, v in number_probs.items() if k >= 5}
        else:
            filtered_probs = {k: v for k, v in number_probs.items() if k < 5}
        
        if not filtered_probs:
            filtered_probs = number_probs
        
        green_numbers = [1, 3, 5, 7, 9]
        red_numbers = [0, 2, 4, 6, 8]
        
        color_freqs = color_analysis.get('frequencies', {})
        green_freq = color_freqs.get('Green', 0.5)
        red_freq = color_freqs.get('Red', 0.5)
        
        if preferred_color:
            if preferred_color == 'Green':
                for k in filtered_probs:
                    if k in green_numbers:
                        filtered_probs[k] *= 1.4
                    else:
                        filtered_probs[k] *= 0.6
            elif preferred_color == 'Red':
                for k in filtered_probs:
                    if k in red_numbers:
                        filtered_probs[k] *= 1.4
                    else:
                        filtered_probs[k] *= 0.6
        else:
            color_bias = green_freq - red_freq
            if abs(color_bias) > 0.1:
                for k in filtered_probs:
                    if color_bias > 0 and k in red_numbers:
                        filtered_probs[k] *= 1.15
                    elif color_bias < 0 and k in green_numbers:
                        filtered_probs[k] *= 1.15
        
        total_prob = sum(filtered_probs.values())
        if total_prob > 0:
            filtered_probs = {k: v / total_prob for k, v in filtered_probs.items()}
        
        sorted_candidates = sorted(filtered_probs.items(), key=lambda x: x[1], reverse=True)
        
        top_number = sorted_candidates[0][0]
        top_prob = sorted_candidates[0][1]
        
        second_prob = sorted_candidates[1][1] if len(sorted_candidates) > 1 else 0
        prob_gap = top_prob - second_prob
        
        number_confidence = min(0.9, 0.5 + prob_gap * 3 + top_prob * 0.2)
        
        overall_confidence = int((big_small_confidence * 0.4 + number_confidence * 0.6) * 100)
        overall_confidence = max(55, min(95, overall_confidence))
        
        predicted_colors = get_number_color(top_number)
        
        return {
            'number': top_number,
            'big_small': predicted_big_small,
            'colors': predicted_colors,
            'confidence': overall_confidence,
            'analysis': {
                'method': ' | '.join(analysis_method) if analysis_method else 'Statistical analysis',
                'top_candidates': [{'number': n, 'score': round(s * 100, 1)} for n, s in sorted_candidates[:3]],
                'streak_info': f"Last {self.big_small_list[:5]}" if len(self.big_small_list) >= 5 else "Limited data"
            }
        }


def generate_prediction(history):
    engine = PredictionEngine(history)
    return engine.predict()


def fetch_current_period():
    try:
        ts = int(time.time() * 1000)
        url = f"{API_BASE}/WinGo/WinGo_30S.json?ts={ts}"
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            data = response.json()
            current = data.get('current', {})
            end_time = current.get('endTime', 0)
            current_time = int(time.time() * 1000)
            left_time = max(0, (end_time - current_time) // 1000)
            
            return {
                'issueNumber': current.get('issueNumber', ''),
                'leftTime': left_time,
                'previous': data.get('previous', {}),
                'next': data.get('next', {})
            }
    except Exception as e:
        print(f"Error fetching current period: {e}")
    return None


history_cache = {
    'data': [],
    'timestamp': 0
}

def fetch_history_page(page=1):
    try:
        ts = int(time.time() * 1000)
        url = f"{API_BASE}/WinGo/WinGo_30S/GetHistoryIssuePage.json?ts={ts}&pageNo={page}&pageSize=50"
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            data = response.json()
            results = []
            
            if isinstance(data, dict) and 'data' in data:
                history_list = data.get('data', {}).get('list', [])
                for item in history_list:
                    period = item.get('issueNumber', '')
                    number = item.get('number', '')
                    color = item.get('color', '')
                    if number != '':
                        results.append({
                            'period': period,
                            'number': number,
                            'big_small': get_big_small(number),
                            'colors': get_color_list(color)
                        })
            return results
    except Exception as e:
        print(f"Error fetching history page {page}: {e}")
    return []

def fetch_history():
    global history_cache
    current_time = int(time.time())
    
    if history_cache['data'] and (current_time - history_cache['timestamp']) < 30:
        return history_cache['data']
    
    all_results = []
    
    for page in range(1, 5):
        page_results = fetch_history_page(page)
        if not page_results:
            break
        all_results.extend(page_results)
        if len(page_results) < 50:
            break
    
    seen_periods = set()
    unique_results = []
    for item in all_results:
        if item['period'] not in seen_periods:
            seen_periods.add(item['period'])
            unique_results.append(item)
    
    unique_results.sort(key=lambda x: x['period'], reverse=True)
    
    if unique_results:
        history_cache['data'] = unique_results
        history_cache['timestamp'] = current_time
    
    return unique_results if unique_results else history_cache['data']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/data')
def get_data():
    current = fetch_current_period()
    history = fetch_history()
    prediction = generate_prediction(history)
    
    return jsonify({
        'next_period': current,
        'history': history[:50],
        'prediction': prediction
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
