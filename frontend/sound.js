function micFunction(){
    event.preventDefault();
    window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    // check if browser supports SpeechRecognition
    if (!window.SpeechRecognition) {
        console.error("Speech recognition not supported in this browser.");
        return;
    }
    const speech = new window.SpeechRecognition();
    console.log("speech = " + speech)
    // enable real-time results
    speech.interimResults = true;
    speech.addEventListener('result',(e) =>{
        console.log("event = " + e)
        const transcript = Array.from(e.results)
                  .flatMap(result => result[0].transcript)
                  .join('');
        console.log("transcript = " + transcript)
        document.getElementById('search-bar').value = transcript;
        searchPhotos()
    })
    speech.start();       
}
