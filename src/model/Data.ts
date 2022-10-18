export class API {
    private static inst: API;

    public static getInstance(): API {
        if (API.inst == null) API.inst = new API();
        return API.inst;
    }

    public gender = 0;
    public age = 0;
    public edu = 0;
    public cvft = 80;

    public cdt = 20;

    public mcog = 0;
    public words = ["apple", "penny", "table"];

    
    public tests = [
        {
            name: "Verbal Test",
            steps: ["CVFT", "Results"]
        },
        {
            name: "Drawing Test",
            steps: ["CDT", "Results"]
        },
        {
            name: "Mini Cognitive Test",
            steps: ["Memory", "CDT", "Recall", "Results"]
        },
        {
            name: "All Tests",
            steps: ["Memory", "CDT", "Recall", "CVFT", "Results"]
        },
    ];
}