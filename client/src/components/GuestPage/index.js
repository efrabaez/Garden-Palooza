import React from "react";
import Phaser from "phaser";
import config from "./JS/phaserJS/game";
import {
  Container,
  Wrap,
  Window,
  Chat
} from "./GuestPage";

const GuestPage = () => {

   React.useEffect(()=>{
   window.game = new Phaser.Game(config);
//     new Phaser.Game(config);
   },[])

  return (
    <>
      <Container>
        <Wrap>
            <Window id="phaser"/>
        </Wrap>
      </Container>
      <Chat>
          <div>Chat Window Sample</div>
        </Chat>
    </>
  );
};

export default GuestPage;
