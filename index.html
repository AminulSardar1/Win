<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WinGo 30S Prediction Engine</title>
    <!-- Load Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Load Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        /* Define custom colors and fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap');
        :root {
            font-family: 'Inter', sans-serif;
        }
    </style>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'primary-green': '#10b981',
                        'primary-red': '#ef4444',
                        'primary-violet': '#8b5cf6',
                        'primary-bg': '#f9fafb',
                    }
                }
            }
        }
    </script>
</head>
<body class="bg-gray-100 min-h-screen p-2 sm:p-4">

    <div id="app" class="max-w-4xl mx-auto">
        <header class="bg-white shadow-lg rounded-xl p-4 mb-4">
            <h1 class="text-3xl font-extrabold text-gray-800 flex items-center">
                <i data-lucide="gem" class="w-8 h-8 text-primary-green mr-2"></i>
                WinGo 30S Predictor
            </h1>
            <p class="text-sm text-gray-500 mt-1">Advanced Pattern Analysis for Next Period</p>
        </header>

        <!-- Current Period & Countdown Section -->
        <section id="current-period-section" class="mb-6 grid grid-cols-1 md:grid-cols-3 gap-4">
            <!-- Prediction Card -->
            <div id="prediction-card" class="md:col-span-2 bg-white p-6 rounded-xl shadow-lg border-t-4 border-primary-green transition-all duration-300">
                <div class="flex justify-between items-center mb-4">
                    <h2 class="text-xl font-bold text-gray-700">Next Predicted Result</h2>
                    <span id="prediction-confidence" class="px-3 py-1 text-sm font-semibold rounded-full bg-primary-green text-white shadow-md"></span>
                </div>
                
                <div class="flex flex-col sm:flex-row items-center justify-between space-y-4 sm:space-y-0 sm:space-x-4">
                    <!-- Predicted Number -->
                    <div class="flex flex-col items-center w-full sm:w-auto">
                        <span class="text-xs font-medium text-gray-500 uppercase">Number</span>
                        <div id="predicted-number" class="text-6xl font-black mt-1 p-4 rounded-xl text-white shadow-2xl transition-transform duration-500 transform hover:scale-105" style="background-color: #374151;">?</div>
                    </div>

                    <!-- Predicted Big/Small & Color -->
                    <div class="flex flex-col space-y-3 w-full sm:w-auto">
                        <div class="bg-gray-50 p-3 rounded-lg flex justify-between items-center shadow-inner">
                            <span class="text-sm font-medium text-gray-500 flex items-center"><i data-lucide="scale" class="w-4 h-4 mr-2"></i> Big/Small:</span>
                            <span id="predicted-big-small" class="text-lg font-bold text-gray-800">...</span>
                        </div>
                        <div class="bg-gray-50 p-3 rounded-lg flex justify-between items-center shadow-inner">
                            <span class="text-sm font-medium text-gray-500 flex items-center"><i data-lucide="paintbrush" class="w-4 h-4 mr-2"></i> Color:</span>
                            <div id="predicted-colors" class="text-lg font-bold flex space-x-1"></div>
                        </div>
                    </div>
                </div>

                <div class="mt-4 pt-4 border-t border-gray-100">
                    <p class="text-xs text-gray-500 italic" id="analysis-reason">Loading prediction analysis...</p>
                </div>
            </div>

            <!-- Countdown Card -->
            <div class="bg-white p-6 rounded-xl shadow-lg flex flex-col justify-between">
                <h2 class="text-xl font-bold text-gray-700 flex items-center"><i data-lucide="clock" class="w-5 h-5 mr-2 text-blue-500"></i> Next Draw</h2>
                <div class="flex flex-col items-center my-4">
                    <span id="next-issue-number" class="text-sm font-mono text-gray-500 bg-gray-100 px-3 py-1 rounded-full mb-2">#00000000</span>
                    <div id="countdown-timer" class="text-7xl font-extrabold text-red-600 animate-pulse">00</div>
                    <span class="text-xs font-medium text-gray-500 uppercase mt-1">Seconds Left</span>
                </div>
                <div class="bg-blue-50 p-3 rounded-lg">
                    <p class="text-sm text-blue-800">Data last updated <span id="last-updated" class="font-semibold">...</span></p>
                </div>
            </div>
        </section>

        <!-- History Table Section -->
        <section class="bg-white p-4 rounded-xl shadow-lg mb-6">
            <h2 class="text-xl font-bold text-gray-700 mb-4 flex items-center"><i data-lucide="list-ordered" class="w-5 h-5 mr-2 text-gray-600"></i> Recent History (Top 20)</h2>
            <div class="overflow-x-auto">
                <table class="min-w-full divide-y divide-gray-200">
                    <thead class="bg-gray-50">
                        <tr>
                            <th class="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Period</th>
                            <th class="px-4 py-2 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">Result</th>
                            <th class="px-4 py-2 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">Big/Small</th>
                            <th class="px-4 py-2 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">Colors</th>
                        </tr>
                    </thead>
                    <tbody id="history-table-body" class="bg-white divide-y divide-gray-200">
                        <!-- History rows will be injected here -->
                    </tbody>
                </table>
            </div>
        </section>
    </div>

    <script>
        // --- CONSTANTS ---
        const API_BASE = "https://draw.ar-lottery01.com";
        const API_VERSION = "WinGo/WinGo_30S"; // Base path for 30S game
        const UPDATE_INTERVAL = 1000; // 1 second update
        const DATA_REFRESH_INTERVAL = 15000; // 15 seconds data refresh

        const NUMBER_TO_COLOR = {
            0: ['primary-red', 'primary-violet'], // Red, Violet
            1: ['primary-green'], // Green
            2: ['primary-red'], // Red
            3: ['primary-green'], // Green
            4: ['primary-red'], // Red
            5: ['primary-green', 'primary-violet'], // Green, Violet
            6: ['primary-red'], // Red
            7: ['primary-green'], // Green
            8: ['primary-red'], // Red
            9: ['primary-green'] // Green
        };

        // --- HELPER FUNCTIONS ---

        /**
         * @param {number} number
         * @returns {'Big' | 'Small'}
         */
        function getBigSmall(number) {
            return number >= 5 ? 'Big' : 'Small';
        }

        /**
         * @param {number} number
         * @returns {string[]} Tailwind color class names
         */
        function getNumberColorClasses(number) {
            return NUMBER_TO_COLOR[number] || ['bg-gray-500'];
        }

        /**
         * Converts API color strings to internal format (and handles unknown)
         * @param {string} colorString
         * @returns {string[]}
         */
        function getColorList(colorString) {
            const colors = [];
            if (colorString.toLowerCase().includes('green')) colors.push('Green');
            if (colorString.toLowerCase().includes('red')) colors.push('Red');
            if (colorString.toLowerCase().includes('violet')) colors.push('Violet');
            return colors.length ? colors : ['Unknown'];
        }

        /**
         * Helper to safely make API calls with retries
         * @param {string} url
         * @param {number} retries
         * @returns {Promise<any>}
         */
        async function fetchWithRetry(url, retries = 3) {
            const headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
            };

            for (let i = 0; i < retries; i++) {
                try {
                    const response = await fetch(url, { headers, timeout: 5000 });
                    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
                    return await response.json();
                } catch (error) {
                    console.error(`Fetch attempt ${i + 1} failed for ${url}:`, error);
                    if (i === retries - 1) throw error;
                    await new Promise(resolve => setTimeout(resolve, Math.pow(2, i) * 1000)); // Exponential backoff
                }
            }
        }


        // --- DATA FETCHING ---

        let currentPeriodData = {
            issueNumber: '00000000',
            leftTime: 0,
            previous: null,
            next: null
        };

        let historyCache = {
            data: [],
            timestamp: 0
        };

        async function fetchCurrentPeriod() {
            try {
                const ts = Date.now();
                const url = `${API_BASE}/${API_VERSION}.json?ts=${ts}`;
                const data = await fetchWithRetry(url);

                const current = data.current || {};
                const endTime = current.endTime || 0;
                const currentTime = Date.now();
                const leftTime = Math.max(0, Math.floor((endTime - currentTime) / 1000));

                currentPeriodData = {
                    issueNumber: current.issueNumber || '00000000',
                    leftTime: leftTime,
                    previous: data.previous || null,
                    next: data.next || null
                };

            } catch (e) {
                console.error("Failed to fetch current period:", e);
                // Keep the old data but reset the timer to ensure refresh
                currentPeriodData.leftTime = 0; 
            }
        }

        async function fetchHistory() {
            const currentTime = Date.now();

            if (historyCache.data.length > 0 && (currentTime - historyCache.timestamp) < DATA_REFRESH_INTERVAL) {
                return historyCache.data;
            }

            let allResults = [];
            // Fetch multiple pages for better statistical analysis
            for (let page = 1; page <= 5; page++) {
                try {
                    const ts = Date.now();
                    const url = `${API_BASE}/${API_VERSION}/GetHistoryIssuePage.json?ts=${ts}&pageNo=${page}&pageSize=50`;
                    const data = await fetchWithRetry(url);

                    const historyList = data?.data?.list || [];
                    const pageResults = historyList
                        .filter(item => item.number !== null && item.number !== '')
                        .map(item => ({
                            period: item.issueNumber,
                            number: parseInt(item.number, 10),
                            big_small: getBigSmall(parseInt(item.number, 10)),
                            colors: getColorList(item.color)
                        }));

                    if (pageResults.length === 0) break;
                    allResults.push(...pageResults);

                } catch (e) {
                    console.error(`Failed to fetch history page ${page}:`, e);
                    break;
                }
            }

            // Deduplicate and sort
            const seenPeriods = new Set();
            const uniqueResults = allResults.filter(item => {
                if (seenPeriods.has(item.period)) return false;
                seenPeriods.add(item.period);
                return true;
            }).sort((a, b) => b.period - a.period); // Sort descending by period number

            if (uniqueResults.length > 0) {
                historyCache.data = uniqueResults;
                historyCache.timestamp = currentTime;
            }
            
            return historyCache.data;
        }


        // --- PREDICTION LOGIC (JS Class Translation of Python) ---

        class PredictionEngine {
            /**
             * @param {Array<Object>} history - Array of historical draw objects
             */
            constructor(history) {
                this.history = history;
                this.numbers = history.map(h => h.number).filter(n => typeof n === 'number');
                this.bigSmallList = history.map(h => h.big_small).filter(bs => bs);
            }

            analyzeFrequency(window = 50) {
                if (this.numbers.length < 5) {
                    return Array.from({ length: 10 }, (_, i) => ({ number: i, score: 0.1 }));
                }

                const recent = this.numbers.slice(0, Math.min(window, this.numbers.length));
                const counts = {};
                recent.forEach(n => counts[n] = (counts[n] || 0) + 1);
                const total = recent.length;

                const freq = {};
                for (let i = 0; i < 10; i++) {
                    freq[i] = (counts[i] || 0) / total || 0.1;
                }
                return freq;
            }

            analyzeHotCold(hotWindow = 10, coldWindow = 50) {
                if (this.numbers.length < hotWindow) {
                    return Array.from({ length: 10 }, (_, i) => ({ number: i, score: 0.5 }));
                }

                const hotCounts = {};
                this.numbers.slice(0, hotWindow).forEach(n => hotCounts[n] = (hotCounts[n] || 0) + 1);

                const coldCounts = {};
                const coldData = this.numbers.slice(0, Math.min(coldWindow, this.numbers.length));
                coldData.forEach(n => coldCounts[n] = (coldCounts[n] || 0) + 1);

                const scores = {};
                for (let i = 0; i < 10; i++) {
                    const hotFreq = (hotCounts[i] || 0) / hotWindow;
                    const coldFreq = (coldCounts[i] || 0) / coldData.length;

                    if (hotFreq > coldFreq * 1.5) {
                        scores[i] = 0.7; // Hot
                    } else if (hotFreq < coldFreq * 0.5) {
                        scores[i] = 0.6; // Cold (due for a hit)
                    } else {
                        scores[i] = 0.5; // Neutral
                    }
                }
                return scores;
            }

            analyzeStreaks() {
                if (this.bigSmallList.length < 3) {
                    return { predicted: null, strength: 0 };
                }

                let streakCount = 1;
                const streakValue = this.bigSmallList[0];

                for (let i = 1; i < Math.min(10, this.bigSmallList.length); i++) {
                    if (this.bigSmallList[i] === streakValue) {
                        streakCount++;
                    } else {
                        break;
                    }
                }

                if (streakCount >= 4) {
                    return {
                        predicted: streakValue === 'Big' ? 'Small' : 'Big',
                        strength: Math.min(0.85, 0.6 + streakCount * 0.05)
                    };
                } else if (streakCount >= 3) {
                    return {
                        predicted: streakValue === 'Big' ? 'Small' : 'Big',
                        strength: 0.7
                    };
                }

                return { predicted: null, strength: 0 };
            }

            analyzeTransitions() {
                if (this.numbers.length < 10) {
                    return {};
                }

                const transitions = {};
                for (let i = 0; i < 10; i++) { transitions[i] = {}; for (let j = 0; j < 10; j++) transitions[i][j] = 0; }

                for (let i = 0; i < this.numbers.length - 1; i++) {
                    const prevNumber = this.numbers[i + 1];
                    const currNumber = this.numbers[i];
                    transitions[prevNumber][currNumber] = (transitions[prevNumber][currNumber] || 0) + 1;
                }

                const transProb = {};
                for (let i = 0; i < 10; i++) {
                    const total = Object.values(transitions[i]).reduce((sum, count) => sum + count, 0);
                    transProb[i] = {};
                    for (let j = 0; j < 10; j++) {
                        transProb[i][j] = (transitions[i][j] || 0) / total || 0.1;
                    }
                }

                return transProb;
            }

            analyzeAlternatingPattern() {
                if (this.bigSmallList.length < 6) {
                    return { isAlternating: false, next: null, strength: 0 };
                }

                const recent = this.bigSmallList.slice(0, 6);
                let alternatingCount = 0;
                for (let i = 0; i < recent.length - 1; i++) {
                    if (recent[i] !== recent[i + 1]) {
                        alternatingCount++;
                    }
                }

                if (alternatingCount >= 4) {
                    const nextVal = recent[0] === 'Big' ? 'Small' : 'Big';
                    return {
                        isAlternating: true,
                        next: nextVal,
                        strength: 0.65 + (alternatingCount - 4) * 0.05
                    };
                }

                return { isAlternating: false, next: null, strength: 0 };
            }

            analyzeColorPatterns() {
                if (this.history.length < 10) {
                    return { frequencies: { Green: 0.5, Red: 0.5, Violet: 0.2 }, streak: null };
                }

                const colorCounts = { Green: 0, Red: 0, Violet: 0 };
                let total = 0;

                this.history.slice(0, 50).forEach(h => {
                    h.colors.forEach(c => {
                        if (c in colorCounts) colorCounts[c]++;
                    });
                    total++;
                });

                const recentPrimaryColors = this.history.slice(0, 10)
                    .map(h => {
                        if (h.colors.includes('Green')) return 'Green';
                        if (h.colors.includes('Red')) return 'Red';
                        return null;
                    })
                    .filter(c => c !== null);

                let colorStreak = null;
                if (recentPrimaryColors.length >= 4) {
                    if (recentPrimaryColors.slice(0, 4).every(c => c === 'Green')) {
                        colorStreak = 'Red'; // Predict reversal
                    } else if (recentPrimaryColors.slice(0, 4).every(c => c === 'Red')) {
                        colorStreak = 'Green'; // Predict reversal
                    }
                }

                const freqs = {
                    Green: (colorCounts.Green / total) || 0.33,
                    Red: (colorCounts.Red / total) || 0.33,
                    Violet: (colorCounts.Violet / total) || 0.05,
                };

                return { frequencies: freqs, streak: colorStreak };
            }

            analyzeGapPattern() {
                if (this.numbers.length < 20) {
                    return Array.from({ length: 10 }, (_, i) => ({ number: i, score: 0.5 }));
                }

                const lastSeen = {};
                this.numbers.forEach((num, idx) => {
                    if (!(num in lastSeen)) lastSeen[num] = idx;
                });

                const gapScores = {};
                for (let i = 0; i < 10; i++) {
                    const gap = lastSeen[i] === undefined ? 20 : lastSeen[i];
                    if (gap >= 15) {
                        gapScores[i] = 0.8; // Very cold, high probability to appear
                    } else if (gap >= 10) {
                        gapScores[i] = 0.7;
                    } else if (gap >= 7) {
                        gapScores[i] = 0.6;
                    } else {
                        gapScores[i] = 0.3; // Very hot, low probability to appear
                    }
                }

                return gapScores;
            }

            calculateNumberProbabilities() {
                if (this.numbers.length < 5) {
                    const randomProbs = {};
                    for(let i=0; i<10; i++) randomProbs[i] = 0.1;
                    return randomProbs;
                }

                const freqScores = this.analyzeFrequency();
                const hotColdScores = this.analyzeHotCold();
                const gapScores = this.analyzeGapPattern();
                const transProbs = this.analyzeTransitions();

                const lastNumber = this.numbers[0] || 0;
                const transScores = transProbs[lastNumber] || Array.from({ length: 10 }, (_, i) => ({ number: i, score: 0.1 }));

                let combined = {};
                for (let i = 0; i < 10; i++) {
                    const score = (
                        (freqScores[i] || 0.1) * 0.15 +
                        (hotColdScores[i] || 0.5) * 0.25 +
                        (gapScores[i] || 0.5) * 0.35 +
                        (transScores[i] || 0.1) * 0.25
                    );
                    combined[i] = score;
                }

                const total = Object.values(combined).reduce((sum, v) => sum + v, 0);
                if (total > 0) {
                    for (const k in combined) {
                        combined[k] /= total;
                    }
                }

                return combined;
            }

            predict() {
                if (this.numbers.length < 5) {
                    const num = Math.floor(Math.random() * 10);
                    return {
                        number: num,
                        big_small: getBigSmall(num),
                        colors: getNumberColorClasses(num),
                        confidence: 50,
                        analysis: {
                            method: 'Random Selection',
                            reason: 'Insufficient data for statistical analysis. Need at least 5 periods.',
                            top_candidates: []
                        }
                    };
                }

                const streakAnalysis = this.analyzeStreaks();
                const alternatingAnalysis = this.analyzeAlternatingPattern();
                const colorAnalysis = this.analyzeColorPatterns();
                let numberProbs = this.calculateNumberProbabilities();

                let predictedBigSmall = null;
                let bigSmallConfidence = 0;
                const analysisMethod = [];
                let preferredColor = colorAnalysis.streak;

                // 1. Big/Small Prediction
                if (streakAnalysis.strength > 0.6) {
                    predictedBigSmall = streakAnalysis.predicted;
                    bigSmallConfidence = streakAnalysis.strength;
                    analysisMethod.push(`Streak Reversal: Expected ${predictedBigSmall}`);
                }

                if (alternatingAnalysis.isAlternating && alternatingAnalysis.strength > bigSmallConfidence) {
                    predictedBigSmall = alternatingAnalysis.next;
                    bigSmallConfidence = alternatingAnalysis.strength;
                    analysisMethod.push(`Alternating Pattern: Expected ${predictedBigSmall}`);
                }

                if (!predictedBigSmall) {
                    const recentList = this.bigSmallList.slice(0, 20);
                    const bigCount = recentList.filter(v => v === 'Big').length;
                    const smallCount = recentList.filter(v => v === 'Small').length;

                    if (bigCount > smallCount + 2) {
                        predictedBigSmall = 'Small';
                        bigSmallConfidence = 0.6;
                        analysisMethod.push("Big/Small Imbalance: Expected Small");
                    } else if (smallCount > bigCount + 2) {
                        predictedBigSmall = 'Big';
                        bigSmallConfidence = 0.6;
                        analysisMethod.push("Big/Small Imbalance: Expected Big");
                    } else {
                        predictedBigSmall = bigCount >= smallCount ? 'Small' : 'Big'; // Predict reversal if balanced
                        bigSmallConfidence = 0.55;
                        analysisMethod.push("Statistical Balance Prediction");
                    }
                }

                // 2. Number Probability Filtering (Filter by Big/Small)
                let filteredProbs = {};
                for (const k in numberProbs) {
                    if (getBigSmall(parseInt(k)) === predictedBigSmall) {
                        filteredProbs[k] = numberProbs[k];
                    }
                }

                if (Object.keys(filteredProbs).length === 0) {
                    filteredProbs = numberProbs;
                }

                // 3. Color Biasing
                const greenNumbers = [1, 3, 5, 7, 9];
                const redNumbers = [0, 2, 4, 6, 8];
                const colorFreqs = colorAnalysis.frequencies;
                const greenFreq = colorFreqs.Green || 0.5;
                const redFreq = colorFreqs.Red || 0.5;

                if (preferredColor) {
                    const multiplier = 1.4;
                    const antiMultiplier = 0.6;
                    analysisMethod.push(`${preferredColor} Color Bias (Streak Reversal)`);

                    for (const k in filteredProbs) {
                        const num = parseInt(k);
                        if (preferredColor === 'Green' && greenNumbers.includes(num)) {
                            filteredProbs[k] *= multiplier;
                        } else if (preferredColor === 'Red' && redNumbers.includes(num)) {
                            filteredProbs[k] *= multiplier;
                        } else {
                            filteredProbs[k] *= antiMultiplier;
                        }
                    }
                } else {
                    // Bias towards the underrepresented color
                    const colorBias = greenFreq - redFreq;
                    if (Math.abs(colorBias) > 0.1) {
                        for (const k in filteredProbs) {
                            const num = parseInt(k);
                            if (colorBias > 0 && redNumbers.includes(num)) { // Green is hot, favor Red
                                filteredProbs[k] *= 1.15;
                                analysisMethod.push("Red Color Bias (Green Overrepresented)");
                            } else if (colorBias < 0 && greenNumbers.includes(num)) { // Red is hot, favor Green
                                filteredProbs[k] *= 1.15;
                                analysisMethod.push("Green Color Bias (Red Overrepresented)");
                            }
                        }
                    }
                }


                // 4. Final Normalization and Selection
                const totalProb = Object.values(filteredProbs).reduce((sum, v) => sum + v, 0);
                if (totalProb > 0) {
                    for (const k in filteredProbs) {
                        filteredProbs[k] /= totalProb;
                    }
                }

                const sortedCandidates = Object.entries(filteredProbs)
                    .map(([n, s]) => ({ number: parseInt(n), score: s }))
                    .sort((a, b) => b.score - a.score);

                const topCandidate = sortedCandidates[0] || { number: 0, score: 0 };
                const topNumber = topCandidate.number;
                const topProb = topCandidate.score;
                const secondProb = sortedCandidates[1]?.score || 0;
                const probGap = topProb - secondProb;

                // Confidence calculation
                const numberConfidence = Math.min(0.95, 0.5 + probGap * 3 + topProb * 0.2);
                let overallConfidence = Math.floor((bigSmallConfidence * 0.4 + numberConfidence * 0.6) * 100);
                overallConfidence = Math.max(55, Math.min(95, overallConfidence));

                const predictedColors = getNumberColorClasses(topNumber);

                return {
                    number: topNumber,
                    big_small: predictedBigSmall,
                    colors: predictedColors,
                    confidence: overallConfidence,
                    analysis: {
                        method: analysisMethod.join(' | ') || 'Complex Statistical Synthesis',
                        reason: `Top Candidate (${topNumber}) probability: ${Math.round(topProb * 100)}%`,
                        top_candidates: sortedCandidates.slice(0, 3).map(c => ({
                            number: c.number,
                            score: Math.round(c.score * 1000) / 10
                        }))
                    }
                };
            }
        }

        // --- UI RENDERING ---

        let mainData = {
            next_period: currentPeriodData,
            history: historyCache.data,
            prediction: null
        };

        function renderPrediction(prediction) {
            if (!prediction) return;
            mainData.prediction = prediction;

            const numEl = document.getElementById('predicted-number');
            const bsEl = document.getElementById('predicted-big-small');
            const colorEl = document.getElementById('predicted-colors');
            const confEl = document.getElementById('prediction-confidence');
            const analysisEl = document.getElementById('analysis-reason');

            // Number display
            numEl.textContent = prediction.number;
            numEl.className = 'text-6xl font-black mt-1 p-4 rounded-xl text-white shadow-2xl transition-transform duration-500 transform hover:scale-105';
            prediction.colors.forEach(c => numEl.classList.add(`bg-${c}`));
            if (prediction.colors.length > 1) numEl.classList.add('bg-gradient-to-r', 'from-primary-violet', 'to-primary-green'); // Handle Violet/Green/Red

            // Big/Small
            bsEl.textContent = prediction.big_small;
            bsEl.style.color = prediction.big_small === 'Big' ? 'rgb(234 88 12)' : 'rgb(59 130 246)'; // Orange or Blue

            // Colors
            colorEl.innerHTML = '';
            prediction.colors.forEach(c => {
                const badge = document.createElement('span');
                badge.textContent = c.replace('primary-', '');
                badge.className = `px-2 py-0.5 text-xs font-semibold rounded-full text-white shadow-sm mr-1`;
                badge.classList.add(`bg-${c}`);
                colorEl.appendChild(badge);
            });

            // Confidence
            confEl.textContent = `${prediction.confidence}% Confidence`;
            if (prediction.confidence >= 75) {
                confEl.classList.remove('bg-yellow-500', 'bg-red-500');
                confEl.classList.add('bg-primary-green');
            } else if (prediction.confidence >= 65) {
                confEl.classList.remove('bg-primary-green', 'bg-red-500');
                confEl.classList.add('bg-yellow-500');
            } else {
                confEl.classList.remove('bg-primary-green', 'bg-yellow-500');
                confEl.classList.add('bg-red-500');
            }

            // Analysis
            const candidateList = prediction.analysis.top_candidates.map(c => 
                `<span class="font-bold">${c.number}</span> (${c.score}%)`
            ).join(', ');
            analysisEl.innerHTML = `Method: <span class="font-semibold">${prediction.analysis.method}</span>. Top Candidates: ${candidateList}.`;
        }

        function renderHistoryTable(history) {
            const tbody = document.getElementById('history-table-body');
            tbody.innerHTML = '';

            history.slice(0, 20).forEach(item => {
                const tr = document.createElement('tr');
                tr.className = 'hover:bg-gray-50';

                // Period
                let tdPeriod = document.createElement('td');
                tdPeriod.className = 'px-4 py-2 whitespace-nowrap text-sm font-medium text-gray-900';
                tdPeriod.textContent = item.period;
                tr.appendChild(tdPeriod);

                // Result Number
                let tdNumber = document.createElement('td');
                tdNumber.className = 'px-4 py-2 whitespace-nowrap text-center';
                const colorClasses = getNumberColorClasses(item.number);
                tdNumber.innerHTML = `<span class="inline-flex items-center justify-center h-8 w-8 text-lg font-bold text-white rounded-full bg-${colorClasses[0]}" style="background-color: ${colorClasses.includes('primary-violet') ? 'linear-gradient(to right, #8b5cf6, #10b981)' : ''}">${item.number}</span>`;
                tr.appendChild(tdNumber);

                // Big/Small
                let tdBS = document.createElement('td');
                tdBS.className = 'px-4 py-2 whitespace-nowrap text-center text-sm font-medium';
                tdBS.innerHTML = `<span class="text-sm font-semibold">${item.big_small}</span>`;
                tdBS.style.color = item.big_small === 'Big' ? 'rgb(234 88 12)' : 'rgb(59 130 246)';
                tr.appendChild(tdBS);

                // Colors
                let tdColors = document.createElement('td');
                tdColors.className = 'px-4 py-2 whitespace-nowrap text-center text-sm';
                tdColors.innerHTML = item.colors.map(c => {
                    const colorClass = c === 'Green' ? 'bg-primary-green' : c === 'Red' ? 'bg-primary-red' : 'bg-primary-violet';
                    return `<span class="px-2 py-0.5 text-xs font-medium rounded-full text-white shadow-sm mr-1 ${colorClass}">${c}</span>`;
                }).join('');
                tr.appendChild(tdColors);

                tbody.appendChild(tr);
            });
        }


        function renderCurrentPeriod(data) {
            document.getElementById('next-issue-number').textContent = `#${data.issueNumber}`;
        }

        // --- MAIN LOOP ---

        let countdownInterval;
        let dataRefreshInterval;

        function updateCountdown() {
            if (currentPeriodData.leftTime > 0) {
                currentPeriodData.leftTime--;
                const timerEl = document.getElementById('countdown-timer');
                timerEl.textContent = String(currentPeriodData.leftTime).padStart(2, '0');
                if (currentPeriodData.leftTime <= 5) {
                    timerEl.classList.add('text-red-600', 'animate-pulse');
                } else {
                    timerEl.classList.remove('text-red-600', 'animate-pulse');
                    timerEl.classList.add('text-gray-700');
                }
            } else {
                // Time's up, force data refresh
                clearInterval(countdownInterval);
                document.getElementById('countdown-timer').textContent = '...';
                document.getElementById('next-issue-number').textContent = 'Loading...';
                fetchAndRenderAllData(true); // Force refresh
                startCountdown(); // Restart the cycle
            }
        }

        async function fetchAndRenderAllData(forceHistoryRefresh = false) {
            document.getElementById('last-updated').textContent = 'Refreshing...';
            try {
                // 1. Fetch Current Period (Always fresh)
                await fetchCurrentPeriod();
                renderCurrentPeriod(currentPeriodData);
                
                // 2. Fetch History (Cached or refreshed)
                const history = await fetchHistory(forceHistoryRefresh);
                renderHistoryTable(history);

                // 3. Generate Prediction
                if (history.length > 0) {
                    const engine = new PredictionEngine(history);
                    const prediction = engine.predict();
                    renderPrediction(prediction);
                } else {
                    renderPrediction(null);
                }
                
                document.getElementById('last-updated').textContent = new Date().toLocaleTimeString();
            } catch (error) {
                console.error("Critical error in main data loop:", error);
                document.getElementById('last-updated').textContent = 'Failed to load data';
            }
        }

        function startCountdown() {
            clearInterval(countdownInterval);
            countdownInterval = setInterval(updateCountdown, UPDATE_INTERVAL);
        }

        function initialize() {
            lucide.createIcons(); // Initialize Lucide Icons

            // Initial fetch and render
            fetchAndRenderAllData(true);

            // Set up recurring data refresh (in case timer sync is off)
            dataRefreshInterval = setInterval(() => fetchAndRenderAllData(false), DATA_REFRESH_INTERVAL);

            // Start the countdown timer
            startCountdown();
        }

        window.onload = initialize;
    </script>
</body>
</html>

