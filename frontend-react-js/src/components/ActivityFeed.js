import './ActivityFeed.css';
import ActivityItem from './ActivityItem';

export default function ActivityFeed(props) {
    let content;
    if (props.activities.length === 0) {
      content = <div className='activity_feed_primer'>
        <h3>There are no activities to display</h3>
      </div>
    } else {
      content = <div className='activity_feed_collection'>
      {props.activities.map(activity => {
      return  <ActivityItem setReplyActivity={props.setReplyActivity} setPopped={props.setPopped} key={activity.uuid} activity={activity} />
      })}
      </div>
    };

    return ( <div>{content}</div> );
}