<template>
    <div class="userProfile-wrapper">
        <section class="welcome-user">
            <div class="header">
                Welcome to your profile <span class="username">{{ state.username }}</span>
            </div>
        </section>
        <section class="addNewPost">
            <AddPost />
        </section>
        <section class="userPosts">
            <SupPost />
        </section>
    </div>
</template>
<script>
import { reactive } from "vue";
import SupPost from "../components/userProfile/SupPost";
import AddPost from "../components/userProfile/AddPost";
export default {
    name: "UserProfile",
    components: { SupPost, AddPost },
    setup() {
        const state = reactive({
            username: JSON.parse(localStorage.getItem("user"))["username"]
        });
        return {
            state
        };
    }
};
</script>
