const Traveller = function(journeys) {
  this.journeys = journeys;
};

Traveller.prototype.getJourneyStartLocations = function() {
    return this.journeys.map((journey) => {
      return journey.startLocation;
    });
};

Traveller.prototype.getJourneyEndLocations = function () {
  return this.journeys.map((journey) => {
    return journey.endLocation;
  });
};

Traveller.prototype.getJourneysByTransport = function (transport) {
  return this.journeys.filter((journey) => {
      return transport === journey.transport
  })
};

Traveller.prototype.getJourneysByMinDistance = function (minDistance) {
  return this.journeys.filter((journey) => {
    return minDistance <= journey.distance
    })
};

Traveller.prototype.calculateTotalDistanceTravelled = function () {
  return this.journeys.reduce((total, journey) => {
        return total + journey.distance
      }, 0)
};

Traveller.prototype.getAllTransport = function () {
  return this.journeys.map((journey) => {
    return journey.transport;
  });
}

Traveller.prototype.getUniqueModesOfTransport = function () {
  transportList = this.getAllTransport();
  return new Set(transportList)
  };


module.exports = Traveller;
