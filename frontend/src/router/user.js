import SignUp from "../views/SignUp.vue";
import LogIn from "../views/LogIn.vue";
export default [
    {
        path: "/signUp",
        name: "SignUp",
        component: SignUp,
        meta: {
            title: "SignUp"
        }
    },
    {
        path: "/logIn",
        name: "LogIn",
        component: LogIn,
        meta: {
            title: "LogIn"
        }
    }
];
