import Gallery from "../views/Gallery.vue";
import SinglePost from "../views/SinglePost.vue";
export default [
    {
        path: "/gallery",
        name: "Gallery",
        component: Gallery,
        meta: {
            title: "Gallery"
        }
    },
    {
        path: "/singlePost/:postId",
        name: "SinglePost",
        component: SinglePost,
        meta: {
            title: "SinglePost"
        }
    }
];
