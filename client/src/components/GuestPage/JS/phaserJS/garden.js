import Phaser from 'phaser';

class Garden extends Phaser.Scene
{
    constructor ()
    {
      debugger
      super({key: "Garden"});
    }

    init (data)
    {
      this.firstLayer = data.firstLayer;
      this.secondLayer = data.secondLayer;
      console.log(this.firstLayer, this.secondLayer)
    }

    preload ()
    {
      debugger
      this.load.image("gardenTile","assets/global.png");
    }

    create ()
    {
      debugger
      let map = this.make.tilemap({ data: this.firstLayer, tileWidth: 16, tileHeight: 16 });
      let map2 = this.make.tilemap({ data: this.secondLayer, tileWidth: 16, tileHeight: 16 })
      let tiles = map.addTilesetImage('gardenTile');
      let tiles2 = map2.addTilesetImage('gardenTile');
      let layer = map.createLayer(0, tiles, 0, 0)
      let layer2 = map2.createLayer(0,tiles2,0,0).setInteractive();
      var self = this;
      layer2.on('pointerdown', function (pointer ) {
        self.scene.stop("Garden") 
        self.scene.start('TileUI')
        let display = document.getElementById("hola")
        let xP = Math.floor(pointer.downX);
        let yP = Math.floor(pointer.downY);
        layer.getTileAtWorldXY(xP,yP).index = 24;
       
      });
    }
}


export default Garden;
