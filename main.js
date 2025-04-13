import init, { fetch_data } from './wasm-test/pkg/wasm_test.js';

async function run() {
    await init();

    async function fetch_wasm_data(){
        try {
            const data = await fetch_data("https://www.random.org/clients/http/api/");
            console.log("Fetched data:", data);
            document.getElementById("result").innerText = data;
        } catch (error) {
            console.error("Error fetching data:", error);
        }
    }
    document.getElementById("calculateButton").addEventListener("click", fetch_wasm_data);
}

run();