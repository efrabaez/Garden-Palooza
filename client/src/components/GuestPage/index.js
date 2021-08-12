import React from "react";
import LoadScene from './JS/phaserJS/loadScene';
import MainScene from './JS/phaserJS/mainScene';
import Phaser from 'phaser';
import {
  Container,
  Wrap,
  Window,
  Chat
} from "./GuestPage";
import './Guest.css'

const config = {
  type: Phaser.AUTO,
  parent: 'phaser',
  width: 800,
  height: 600,
  scene: [ LoadScene, MainScene ]
};

const game = new Phaser.Game(config);

const GuestPage = () => {
  return (
    <>
      <Container>
        <Wrap id="phaser">
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
