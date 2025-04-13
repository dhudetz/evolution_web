use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn calculate_tax(income: f64) -> f64 {
    let tax: f64 = if income <= 9865.0 {
        income * 0.10
    } else if income <= 40125.0 {
        987.5 + (income - 9875.0) * 0.12
    } else if income <= 85525.0 {
        4617.5 + (income - 40125.0) * 0.22
    } else if income <= 163300.0 {
        14605.5 + (income - 85525.0) * 0.24
    } else if income <= 207350.0 {
        33271.5 + (income - 163300.0) * 0.32
    } else if income <= 518400.0 {
        47367.5 + (income - 207350.0) * 0.35
    } else {
        156235.0 + (income - 518400.0) * 0.37
    };
    tax
}