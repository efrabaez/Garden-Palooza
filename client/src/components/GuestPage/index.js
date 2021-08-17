import React from "react";
import Phaser from "phaser";
import config from "./JS/phaserJS/game";
import {
  Container,
  Wrap,
  Window,
  Chat
} from "./GuestPage";

// CHAT COMPONENT
const ChatWrapper = () => {
  const [message, setMessage] = React.useState('')
  const [chats, setChats] = React.useState([
    {username: 'Ainne', message: 'First message'},
    {username: 'Efrain', message: '2nd message'},
  ])

    const handleMessage = (e) => {
        var newMessage = e.currentTarget.value
        // console.log(newMessage)
        setMessage(newMessage)
    }

  React.useEffect(() => {

    // TODO add sock io connection with callback.
    // setChats([...chats, messageFromServer])

    return () => {
      // Stop subscription.
    }
  });


  return (
    <Chat>
      {
        chats.map(chat => (
          <div>{chat.username}: {chat.message}</div>
        ))
      }
      <form onSubmit={(e) => {
        e.preventDefault()
        const formData = new FormData(e.target)
        const message = formData.get('message')
        setChats([...chats, {username: 'Ainne', message}]);
        setMessage("")
        
      }}>
        <input type="text" name="message" value={message} onChange={handleMessage} />
        <button >Send Message</button>
      </form>
    </Chat>
  )
}


//GAME COMPONENT
const GuestPage = () => {

  React.useEffect(()=>{
    window.game = new Phaser.Game(config);
  },[])

  return (
    <>
      <Container>
        <Wrap>
            <Window id="phaser"/>
            <ChatWrapper />
        </Wrap>
      </Container>
    </>
  );
};


export default GuestPage;
