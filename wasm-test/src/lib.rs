use wasm_bindgen::prelude::*;
use web_sys::{Request, RequestInit, RequestMode, Response};
use wasm_bindgen_futures::JsFuture;

#[wasm_bindgen]
pub async fn fetch_data(url: &str) -> Result<String, JsValue> {
    // Get the window object
    let window = web_sys::window().ok_or("No global `window` exists")?;

    // Create a Request object
    let opts = RequestInit::new();
    opts.set_method("GET");
    opts.set_mode(RequestMode::Cors);

    let request = Request::new_with_str_and_init(url, &opts)?;

    // Make the HTTP request
    let response_value = JsFuture::from(window.fetch_with_request(&request)).await?;
    let response: Response = response_value.dyn_into()?;

    // Check if the response was successful
    if !response.ok() {
        return Err(JsValue::from_str(&format!("HTTP error: {}", response.status())));
    }

    // Extract the response text
    let text = JsFuture::from(response.text()?).await?;
    let text_str = text.as_string().ok_or("Failed to convert response to string")?;

    Ok(text_str)
}