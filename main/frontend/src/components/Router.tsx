import { Switch, Route } from "react-router-dom";
import Main from "./Main";
import Profile from "./Profile";
import Login from "./Login";

function Routes() {
  return (
    <Switch>
      <Route exact path="/Profile" component={Main} />
      <Route exact path="/Main" component={Profile} />

      <Route exact path="/Login" component={Main} />
      <Route exact path="/Main" component={Login} />
    </Switch>
  );
}

export default Routes;