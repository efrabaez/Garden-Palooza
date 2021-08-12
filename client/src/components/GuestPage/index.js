import React from "react";
import game from "./JS/phaserJS/game"
import {
  Container,
  Wrap,
  Icon,
  Content,
  Window,
  Game
} from "./GuestPage";

const GuestPage = () => {
  return (
    <>
      <Container>
        <Wrap>
          <Icon to="/">GP</Icon>
          <Content>
            <Window id="phaser">
              <Game id="phaser"></Game>
            </Window>
          </Content>
        </Wrap>
      </Container>
    </>
  );
};

export default GuestPage;
