<template>
    <div class="singlePost-wrapper">
        <div class="singlePost-content">{{ postId }}</div>
    </div>
</template>
<script>
import { useRoute } from "vue-router";
export default {
    name: "SinglePost",
    setup() {
        const route = useRoute();
        const postId = route.params["postId"];

        return {
            postId
        };
    }
};
</script>
