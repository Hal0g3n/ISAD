<template>
    <div class="Memory">
        <h1 class="subheading grey--text">ISAD</h1>


        <v-container>
            <v-row>
                1
            </v-row>
            <v-row>
                2
            </v-row>
            <v-row>
                3
            </v-row>
            <v-btn @click="click"/>
        </v-container>

    </div>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
    data: () => ({}),

    methods: {
        click() {
            this.$emit("complete", "CDT");
        }
    }
});

</script>