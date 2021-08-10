import React from "react";
import LoadScene from './JS/phaserJS/loadScene';
import MainScene from './JS/phaserJS/mainScene';
import Phaser from 'phaser';
import Game from './Game'
import {
  Container,
  Wrap,
  Icon,
  Content,
  Window,
  Games,
} from "./GuestPage";

const config = {
  type: Phaser.AUTO,
  parent: 'phaser',
  width: 400,
  height: 400,
  scene: [ LoadScene, MainScene ]
};

const game = new Phaser.Game(config);

const GuestPage = () => {
  return (
    <>
      <Container>
        <Wrap>
          <Icon to="/">GP</Icon>
          <Content>
            <Window>
              <Games id="phaser">
              </Games>
            </Window>
          </Content>
        </Wrap>
      </Container>
    </>
  );
};

export default GuestPage;
