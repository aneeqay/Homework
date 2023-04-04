const Park = function (name, ticketPrice) {
    this.name = name
    this.ticketPrice = ticketPrice
    this.dinosaurs = []
}

Park.prototype.noOfDinosaurs = function () {
    return this.dinosaurs.length
}

Park.prototype.addDinosaur = function (dinosaur) {
    this.dinosaurs.push(dinosaur)
}

Park.prototype.removeDinosaur = function(dinosaur){
    indexPos = this.dinosaurs.indexOf(dinosaur)
    this.dinosaurs.splice(indexPos,1)
}

Park.prototype.popDino = function () {
    let MostPopDino = this.dinosaurs[0]
    
    for (dinosaur of this.dinosaurs) {
        if (dinosaur.guestsAttractedPerDay > MostPopDino.guestsAttractedPerDay)
        MostPopDino = dinosaur

    }
    return MostPopDino
}

Park.prototype.dinoBySpecies = function (species) {
    let speciesList = []
    for (dinosaur of this.dinosaurs) {
        if (dinosaur.species === species) {
            speciesList.push(dinosaur)
        }
    }
    return speciesList
}

Park.prototype.headCount = function(){
    let count = 0

    for (dinosaur of this.dinosaurs) {
        count += dinosaur.guestsAttractedPerDay
    }

    return count
}

Park.prototype.headCountPerYear = function(){
    let count = 0

    for (dinosaur of this.dinosaurs) {
        count += (dinosaur.guestsAttractedPerDay * 365)
    }

    return count
}

Park.prototype.yearlyTotal = function () {
    return (this.headCountPerYear() * this.ticketPrice)
}

module.exports = Park