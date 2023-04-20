import './ProfileAvatar.css';

export default function ProfileAvatar(props) {
    const backgroundImage = `url("https://assets.sudosam.com/avatars/${props.id}.jpg")`
    const styles = {
        backgroundImage: backgroundImage,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
    };
    console.log("HELLO WORLD")
  return (
    <div 
        className="profile-avatar"
        style={styles}
        ></div>
  );
}