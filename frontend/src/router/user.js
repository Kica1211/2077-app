import SignUp from "../views/SignUp.vue";
import LogIn from "../views/LogIn.vue";
import Logout from "../views/Logout.vue";
import UserProfile from "../views/UserProfile.vue";
import { unauthorized, deepUserAuthorization } from "./_guards";
export default [
    {
        path: "/signUp",
        name: "SignUp",
        component: SignUp,
        meta: {
            title: "SignUp"
        },
        beforeEnter: unauthorized
    },
    {
        path: "/logIn",
        name: "LogIn",
        component: LogIn,
        props: true,
        meta: {
            title: "LogIn"
        },
        beforeEnter: unauthorized
    },
    {
        path: "/userProfile",
        name: "UserProfile",
        component: UserProfile,
        meta: {
            title: "User Profile"
        },
        beforeEnter: deepUserAuthorization
    },
    {
        path: "/logout",
        name: "Logout",
        component: Logout,
        meta: {
            title: "Logout"
        },
        beforeEnter: deepUserAuthorization
    }
];
