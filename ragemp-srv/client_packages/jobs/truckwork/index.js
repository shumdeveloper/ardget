const markerType = 1;
const markerSize = 5;
const markerColor = [0, 255, 0, 100];
const freezeTime = 3000;
const localPlayer = mp.players.local;

let loadPoint = false;
let destPoint = false;

let workMarker = false;
let workBlip = false;
let workMarkerColshape = false;

let missionStatus = 0; // 0 - Dont started, 1 marker, 2 dest marker


mp.events.add('playerStartTruckWork', (startPoint, finishPoint) => {
    if(missionStatus !== 0){
        return mp.gui.chat.push("Hey! You already started this work")
    }

    if(!checkPlayerInVehicleWithTrailer()) return false;

    loadPoint = startPoint
    destPoint = finishPoint

    mp.gui.chat.push('Work on Truck started! Go to marker on map')

    setMarker(startPoint)
    missionStatus = 1;
})

mp.events.add('playerEnterColshape', (colspahe) => {
    if (colspahe === workMarkerColshape){
        pickLocation()
    }
})

function pickLocation(){
    if(!checkPlayerInVehicleWithTrailer()) return false;


    clearMarker();
    freezePlayer();

    if(missionStatus === 1){
        playerReachLoadingPoint()
    } else if (missionStatus === 2){
        playerReachDestPoint()
    }
}

function playerReachLoadingPoint(){
    if(!checkPlayerInVehicleWithTrailer()) return false;

    mp.gui.chat.push("You arrived to loading point! (1/2). Wait...")

    setTimeout( () => {
        unFreezePlayer();
        setMarker(destPoint)
        missionStatus = 2;

        mp.gui.chat.push("Get to unloading place!")

    }, freezeTime)

}

function playerReachDestPoint(){
    if(!checkPlayerInVehicleWithTrailer()) return false;

    mp.gui.chat.push("You arrived to unloading point! (2/2) Wait...")

    setTimeout( () => {
        unFreezePlayer();
        missionStatus = 0;

        mp.gui.chat.push("Wow, you make this! Work ended. Thank`s for work")
    }, freezeTime)


}
function setMarker(point){
    workMarker = mp.markers.new(markerType, point, markerSize, { color: markerColor })
    workMarkerColshape = mp.colshapes.newSphere(point.x, point.y, point.z, 5)
    workBlip = mp.blips.new(67, point, { shortRange: false })
    workBlip.setRoute(true);
}

function clearMarker(){
    workMarker.destroy();
    workMarkerColshape.destroy();
    workBlip.setRoute(false);
    workBlip.destroy();
}

function freezePlayer(){
    localPlayer.freezePosition(true)
    localPlayer.vehicle.freezePosition(true)
}

function unFreezePlayer(){
    localPlayer.freezePosition(false)
    localPlayer.vehicle.freezePosition(false)
}


function checkPlayerInVehicleWithTrailer(){
    if (!localPlayer.vehicle){
        mp.gui.chat.push("You must sit in transport.")
        return false;
    }
    if(!localPlayer.vehicle.isAttachedToTrailer()){
        mp.gui.chat.push("You must have attached trailer!")
        return false;
    }
    if((localPlayer.vehicle.getBodyHealth() < 930)){
        mp.gui.chat.push("You damaged vehicle. Work stopped")
        missionStatus = 0;
        clearMarker()
        localPlayer.vehicle.destroy()

        return false;
    }
    return true
}

mp.events.add("playerLeaveVehicle", (vehicle, seat) => {
    if(missionStatus > 0){
        vehicle.destroy()
        mp.gui.chat.push("You leave truck, work ended.")
        missionStatus = 0
        clearMarker()
    }
})


