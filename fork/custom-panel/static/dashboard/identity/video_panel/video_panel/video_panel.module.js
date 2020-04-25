(function() {
  'use strict';

  angular
    .module('horizon.dashboard.identity.video_panel.video_panel', [])
    .controller('horizon.dashboard.identity.myPluginController',
      myPluginController);

  myPluginController.$inject = [ '$http' ];

  function myPluginController($http) {
    var ctrl = this;
    ctrl.items = [
      { name: 'abc', id: 123 },
      { name: 'efg', id: 345 },
      { name: 'hij', id: 678 }
    ];
  }
})();