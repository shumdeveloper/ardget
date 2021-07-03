// OWN MODE CLIENT
const localPlayer = mp.players.local;

mp.gui.chat.push('Welcome client test!');


mp.events.add("consoleCommand", (command) => {
    if (command === "iadmin") {
        mp.console.logInfo('Checking...')
        if (localPlayer.name !== 'test') {
            mp.console.logInfo('Yeah, you admin')

        }
        if (command === 'myname') {
            mp.console.logInfo('Your name: ' + localPlayer.name)
        }
    }
})

