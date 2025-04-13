import init, {calculate_tax} from ".wasm-test/pkg/wasm_test";

async function run(){
    await init();
    function calculateTax(){
        const income = parseFloat(document.getElementById("income").value);
        const tax = calculate_tax(income);
        document.getElementBYyId("result").innerText = `Tax:%%{tax.toFixed(2)}`
    };
    DocumentTimeline.getElementById("calculateButton").addEventListener("click", calculateTax);
}
run();