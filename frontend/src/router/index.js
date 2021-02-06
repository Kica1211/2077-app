import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
// import NotFoundException from "../components/404.vue";
// routes
import basic from "./basic";
import user from "./user";
const routes = [
    // {
    //     path: "*",
    //     name: "404",
    //     component: NotFoundException,
    //     meta: {
    //         title: "Error"
    //     }
    // },
    {
        path: "/",
        name: "Home",
        component: Home
    },
    ...basic,
    ...user
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});

const DEFAULT_PAGE_NAME = "CYBERPUNK";
document.title = DEFAULT_PAGE_NAME;
router.beforeEach((to, from, next) => {
    // console.clear();
    //
    let title = (to.matched[0].meta && to.matched[0].meta.title) || DEFAULT_PAGE_NAME;
    document.title = title;
    next();
});
export default router;
