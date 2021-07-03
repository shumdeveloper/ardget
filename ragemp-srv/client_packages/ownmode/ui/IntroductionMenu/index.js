// Introduction menu script
let browser;
let browserEnabled = false;

function browserShow(){
    browserEnabled = true;
    browser = mp.browsers.new("http://192.168.1.104:3000") // package://ownmode/ui/IntroductionMenu/build/index.html
    browser.active = true
}


function browserHide() {
    browserEnabled = false;
    browser.active = false
    browser.destroy()
}


// 0x71 is the F2 key code
mp.keys.bind(0x71, true, function () {
    try{
        browser.execute("elementHover('carspawn')");
        mp.events.callRemote('keypress:F2'); // Calling server event "keypress:F2"

    }catch (e){
        mp.gui.chat.push('Open menu on F3.');
    }
});

// F4 key code
mp.keys.bind(0x73, true, function () {
    try{
        browser.execute("elementHover('kill')");
        mp.events.callRemote("keypress:F4")
    }catch (e){
        mp.gui.chat.push('Open menu on F3.');

    }

});

mp.keys.bind(0x72, true, function () {
    if (browserEnabled){
        browserHide()
    }else{
        browserShow()
    }
})
