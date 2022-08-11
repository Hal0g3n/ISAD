<template>
    <div class = "Dashboard">
        <h1 class="subheading grey--text">Homepage</h1>


        <v-container class=my-5>
            
            <!-- First Row in container -->
            <!-- wrap: For overflowing items to go to next row -->
            <v-row wrap>
                <!-- First Item in first row -->
                <v-col cols="12" md="6">
                    <v-btn outline block class=primary>1</v-btn>
                </v-col>

                <!-- Second Items in first row (May overflow) -->
                <v-col cols="4" md="2">
                    <v-btn outline block class=primary>2</v-btn>
                </v-col>
                <v-col cols="4" md="2">
                    <v-btn outline block class=primary>2</v-btn>
                </v-col>
                <v-col cols="4" md="2">
                    <v-btn outline block class=primary>2</v-btn>
                </v-col>

            </v-row>

            <v-row wrap justify=space-between>
                <v-col cols=4 md=3>
                    <v-btn outline block class=success>1</v-btn>
                </v-col>
                <v-col cols=4 md=3>
                    <v-btn outline block class=success>2</v-btn>
                </v-col>
            </v-row>

        </v-container>
    </div>
</template>



<script lang="ts">

import Vue from "vue";

export default Vue.extend({
    name: "HomePage",

    components: {
        //
    },
});

</script>
