// User commands
// ==
// MONEY API



// End Money API


// FOR DEBUG
mp.events.addCommand('vpos', (player) => {
    const {position} = player.vehicle;
    console.log(`{ x: ${position.x}, y: ${position.y}, z: ${position.z}, heading: ${player.vehicle.heading} } `)
})
// END FOR DEBUG