<template>
<div>
    <router-view></router-view>
</div>
</template>

<script>
    import axios from 'axios';
    import { protectedUrlMixin } from '../../../protectedUrlMixin';
    export default {
        data() {
            return {
                
            };
        },
        mixins: [
            protectedUrlMixin
        ],
        methods: {

        }
    }
</script>

<style>

</style>
