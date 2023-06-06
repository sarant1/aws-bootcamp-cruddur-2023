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
  const dataFetchedRef = React.useRef(false);
  const params = useParams();


  

  // const setupWebsocket = () => {
  //   socket = io(`${process.env.REACT_APP_BACKEND_URL}`)
  //   socket.on('connect', () => {
  //   setSocketConnected(true)
  //   console.log("CONNECTED TO WEBSOCKET")
  //   })
  // }

  const sendMessage = () => {
    console.log("TESTING123")
    socket.emit('new message', 'THIS IS WORKING !!')
  }

  React.useEffect(() => {
    socket = io(`${process.env.REACT_APP_BACKEND_URL}`)
    socket.on('connect', () => {
    setSocketConnected(true)
    console.log("CONNECTED TO WEBSOCKE")
    })
  }, [])


  const loadMessageGroupsData = async () => {
    const url = `${process.env.REACT_APP_BACKEND_URL}/api/message_groups`
    get(url,{
      auth: true,
      success: function(data){
        setMessageGroups(data)
      }
    })
  }

  const loadMessageGroupData = async () => {
    const url = `${process.env.REACT_APP_BACKEND_URL}/api/messages/${params.message_group_uuid}`
    get(url,{
      auth: true,
      success: function (data){
        setMessages(data)
      }
    })
  }

  React.useEffect(()=>{
    //prevents double call
    if (dataFetchedRef.current) return;
    dataFetchedRef.current = true;

    loadMessageGroupsData();
    loadMessageGroupData();
    checkAuth(setUser);
  })
  
  return (
    <article>
      <DesktopNavigation user={user} active={'home'} setPopped={setPopped} />
      <section className='message_groups'>
        <MessageGroupFeed message_groups={messageGroups} />
      </section>
      <div className='content messages'>
        <MessagesFeed messages={messages} />
        <MessagesForm setMessages={setMessages}  socket={socket}/>
        <button onClick={sendMessage}>
          SEND MESSAGE
        </button>
      </div>
    </article>
  );
}