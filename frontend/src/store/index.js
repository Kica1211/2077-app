import { createStore } from "vuex";
export const API_ADDRESS = "http://127.0.0.1:8000";
import { auth_module } from "./user/auth";
export default createStore({
    state: {
        API_ADDRESS
    },
    mutations: {},
    actions: {},
    modules: {
        auth_module
    }
});
