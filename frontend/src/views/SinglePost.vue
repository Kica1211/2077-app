<template>
    <div class="singlePost-wrapper">
        <div class="singlePost-content">{{ state.singlePost }}</div>
    </div>
</template>
<script>
import { onMounted, reactive } from "vue";
import { useRoute } from "vue-router";
import { useStore } from "vuex";
import axios from "axios";
export default {
    name: "SinglePost",
    setup() {
        const state = reactive({
            singlePost: []
        });
        const route = useRoute();
        const store = useStore();
        const postId = route.params["postId"];
        const API_ADDRESS = store.state.API_ADDRESS;
        function getSinglePost() {
            axios
                .get(`${API_ADDRESS}/posts/${postId}/`)
                .then(res => (state.singlePost = res.data))
                .catch(err => console.log(err));
        }
        onMounted(() => {
            getSinglePost();
        });
        return {
            postId,
            state
        };
    }
};
</script>
