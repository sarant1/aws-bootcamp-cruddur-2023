import { Auth } from 'aws-amplify';


export const getAccessToken = async () => {
  try {
    const cognito_user = await Auth.currentSession();
    const access_token = cognito_user.accessToken.jwtToken;
    localStorage.setItem('access_token', access_token);
    return access_token;
  } catch (err) {
    console.log(err);
    return null;
  }
};

export const checkAuth = async (setUser) => {
    Auth.currentAuthenticatedUser({
      // Optional, By default is false. 
      // If set to true, this call will send a 
      // request to Cognito to get the latest user data
      bypassCache: false 
    })
    .then((cognito_user) => {
      setUser({
        cognito_user_id: cognito_user.attributes.sub,
        display_name: cognito_user.attributes.name,
        handle: cognito_user.attributes.preferred_username
      })
      return Auth.currentSession()
    }).then((cognito_user_session) => {
      localStorage.setItem("access_token", cognito_user_session.accessToken.jwtToken)
    })
    .catch((err) => console.log(err));
  };
