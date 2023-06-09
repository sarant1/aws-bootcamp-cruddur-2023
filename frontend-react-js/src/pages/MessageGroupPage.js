import './MessageGroupPage.css';
import React from "react";
import { useParams } from 'react-router-dom';

import {get} from 'lib/Requests';
import {checkAuth} from 'lib/CheckAuth';

import DesktopNavigation  from 'components/DesktopNavigation';
import MessageGroupFeed from 'components/MessageGroupFeed';
import MessagesFeed from 'components/MessageFeed';
import MessagesForm from 'components/MessageForm';
import { io } from 'socket.io-client';

var socket;

export default function MessageGroupPage() {
  const [messageGroups, setMessageGroups] = React.useState([]);
  const [messages, setMessages] = React.useState([]);
  const [popped, setPopped] = React.useState([]);
  const [user, setUser] = React.useState(null);
  const [socketConnected, setSocketConnected] = React.useState(false);
  const [didJoinRoom, setDidJoinRoom] = React.useState(false);
  const dataFetchedRef = React.useRef(false);
  const params = useParams();


  

  // This will join the chat if user is defined and they are not already in the room
  if (user && !didJoinRoom) {
    const data = {
      "username": user.handle,
      "room": params.message_group_uuid
    };
    socket.emit('join', data);
    console.log("successfully joined room")
    setDidJoinRoom(true)
  }

  React.useEffect( () => {
    checkAuth(setUser)
    socket = io(`${process.env.REACT_APP_BACKEND_URL}`)
    socket.on('connect',  () => {
      console.log("Connected to websocket server")

      socket.on('new message', (data) => {
        console.log('new message:',data)
        setMessages(current => [...current, data])
      })
    })
  }, [])

  React.useEffect(()=>{
    //prevents double call
    if (dataFetchedRef.current) return;
    dataFetchedRef.current = true;

    loadMessageGroupsData();
    loadMessageGroupData();

  }, [])


  


  async function loadMessageGroupData () {
    const url = `${process.env.REACT_APP_BACKEND_URL}/api/messages/${params.message_group_uuid}`
    get(url,{
      auth: true,
      success: function (data){
        setMessages(data)
      }
    })

  }

  

  const loadMessageGroupsData = async () => {
    const url = `${process.env.REACT_APP_BACKEND_URL}/api/message_groups`
    get(url,{
      auth: true,
      success: function(data){
        setMessageGroups(data)
      }
    })
  }

  
  
  return (
    <article>
      <DesktopNavigation user={user} active={'home'} setPopped={setPopped} />
      <section className='message_groups'>
        <MessageGroupFeed message_groups={messageGroups} socket={socket}/>
      </section>
      <div className='content messages'>
        <MessagesFeed messages={messages} />
        <MessagesForm setMessages={setMessages}  socket={socket} setUser={setUser} user={user}/>
      </div>
    </article>
  );
}