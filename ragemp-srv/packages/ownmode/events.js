let spawnPoints = require('./spawn_points.json').SpawnPoints;
let DB = require('./core/database')


// =====================
// Death event

mp.events.add('playerDeath', (player) => {
    player.spawn(spawnPoints[Math.floor(Math.random() * spawnPoints.length)]);
    player.health = 100;
});

// =====================

// Player Ready Event

mp.events.add('playerReady', (player) => {
    player.call('showLoginDialog');
})

// =====================
// Key presses

mp.events.add('keypress:F4', (player) => {
    player.health = 0;
})

mp.events.add('keypress:F2', (player) => {
    mp.vehicles.new('deluxe', player.position)
    player.outputChatBox("Car Spawned! :)")
})

// End of key presses
// =====================


mp.events.add("serverShutdown", async () => {
    DB.end()
    console.log("-- DB Connection Ended")
})