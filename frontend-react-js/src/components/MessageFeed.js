import { useEffect, useRef } from 'react';
import './MessageFeed.css';
import MessageItem from './MessageItem';

export default function MessageFeed(props) {

  const messagesRef = useRef(null);

  useEffect(() => {
    scrollToBottom();
  }, [props.messages])

  const scrollToBottom = () => {
    if (messagesRef.current) {
      messagesRef.current.scrollIntoView({ behavior: 'smooth', block: 'end' });
    }
  };

  return (
    <div className='message_feed'>
      <div className='message_feed_heading'>
        <div className='title'>Messages</div>
      </div>
      <div className='message_feed_collection' >
        {props.messages.map(message => {
        return  <MessageItem key={message.uuid} message={message} />
        })}
      </div>

      <div ref={messagesRef} />
    </div>
  );
}