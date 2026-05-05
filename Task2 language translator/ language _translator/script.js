// 🌍 Language List (International + Indian)
const languages = {
    "en": "English",
    "hi": "Hindi",
    "mr": "Marathi",
    "kn": "Kannada",
    "ta": "Tamil",
    "te": "Telugu",
    "ml": "Malayalam",
    "bn": "Bengali",
    "gu": "Gujarati",
    "pa": "Punjabi",
    "ur": "Urdu",

    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "ru": "Russian",
    "ja": "Japanese",
    "ko": "Korean",
    "zh": "Chinese",
    "ar": "Arabic",
    "tr": "Turkish",
    "nl": "Dutch",
    "pl": "Polish",
    "sv": "Swedish",
    "fi": "Finnish",
    "no": "Norwegian",
    "da": "Danish",
    "th": "Thai",
    "vi": "Vietnamese",
    "id": "Indonesian"
};

// 🔽 Populate dropdowns automatically
const sourceSelect = document.getElementById("sourceLang");
const targetSelect = document.getElementById("targetLang");

for (let code in languages) {
    let option1 = new Option(languages[code], code);
    let option2 = new Option(languages[code], code);

    sourceSelect.add(option1);
    targetSelect.add(option2);
}

// Default selections
sourceSelect.value = "en";
targetSelect.value = "hi";

// 🔁 Translate Function
async function translateText() {
    let text = document.getElementById("inputText").value;
    let source = sourceSelect.value;
    let target = targetSelect.value;

    if (text === "") {
        alert("Please enter text!");
        return;
    }

    let url = `https://api.mymemory.translated.net/get?q=${text}&langpair=${source}|${target}`;

    let response = await fetch(url);
    let data = await response.json();

    document.getElementById("outputText").value =
        data.responseData.translatedText;
}

// 📋 Copy
function copyText() {
    let output = document.getElementById("outputText");
    output.select();
    document.execCommand("copy");
    alert("Copied!");
}

// 🔊 Speak
function speakText() {
    let text = document.getElementById("outputText").value;

    if (text === "") {
        alert("Nothing to speak!");
        return;
    }

    let speech = new SpeechSynthesisUtterance(text);
    speech.lang = targetSelect.value;
    speechSynthesis.speak(speech);
}