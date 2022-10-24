import {reactive} from "vue";

/**
 * Globally accessible data will be available here (all reactive)
 */

export const data = reactive({
    // Some information on the user
    gender: 0,
    age: 0,
    edu: 0,
    steps: [],

    scores: {} as { [key: string]: number; },
    
    words: ["apple", "penny", "table"],
    
    tests: [
        {
            name: "Verbal Test",
            steps: ["CVFT", "Results"]
        },
        {
            name: "Drawing Test",
            steps: ["CDT", "Results"]
        },
        {
            name: "MiniCog Test",
            steps: ["Memory", "CDT", "Recall", "Results"]
        },
        {
            name: "All Tests",
            steps: ["Memory", "CDT", "Recall", "CVFT", "Results"]
        },
    ],
});