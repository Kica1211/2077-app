<template>
    <div class="home-content">
        <div class="posts-set" v-for="item in state.numberOfSets" v-bind:key="item">
            <div class="single-post" v-for="(post, key) in state.posts.slice((item - 1) * 9, item * 9)" v-bind:key="key">
                <router-link :to="{ path: `/singlePost/${post.id}` }">
                    <div class="single-post-image" v-bind:style="{ backgroundImage: `url(${post.main_image})` }"></div>
                    <div class="single-post-data">
                        <div class="title">{{ addDots(post.title) }}</div>
                        <div class="date">{{ formatDate(post.created) }}</div>
                    </div>
                </router-link>
            </div>
        </div>
        <!-- {{ state.numberOfSets < (state.posts.length % 9) + 1 }} -->
        <button class="load-more-posts" v-if="state.numberOfSets < state.posts.length / 9" v-on:click="increaseNumberOfSets">
            Load more news
        </button>
    </div>
</template>
<script>
// import { posts } from "../../assets/posts";
import { reactive, onMounted } from "vue";
import axios from "axios";
import { useStore } from "vuex";
export default {
    name: "HomeContent",
    setup() {
        const state = reactive({
            // posts,
            posts: [],
            numberOfSets: 1
        });
        const store = useStore();
        const API_ADDRESS = store.state.API_ADDRESS;
        function getPosts() {
            axios
                .get(`${API_ADDRESS}/posts/`)
                .then(res => (state.posts = res.data))
                .catch(err => console.log(err));
        }

        function increaseNumberOfSets() {
            state.numberOfSets += 1;
        }

        function addDots(word) {
            if (word.length > 35) {
                return word.slice(0, 35) + "...";
            } else {
                return word;
            }
        }

        function formatDate(date) {
            const result = date.slice(0, 10);
            return result.slice(8, 10) + "." + result.slice(5, 7) + "." + result.slice(0, 4);
        }

        onMounted(() => {
            getPosts();
        });
        return {
            state,
            increaseNumberOfSets,
            addDots,
            formatDate
        };
    }
};
</script>
