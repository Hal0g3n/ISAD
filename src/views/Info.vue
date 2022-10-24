<template> <div class="Info"> 

    <!-- Getting Personal Information -->
    <v-container fill-height key="details">
        <h1>Details</h1>

        <v-row>
            <v-col cols=12>
                <h2 class="subheading grey--text mb-2">Gender</h2>
                <v-select
                    label="Select Your Gender"

                    item-text="sex"
                    item-value="val"
                    :items="[{sex: 'Male', val: 0}, {sex: 'Female', val: 1}]"
                    v-model="gender"

                    :rules="[(v) => v.val!=-1 || 'Please Select a Gender']"
                    required

                    outlined>

                </v-select>

            </v-col>
        </v-row>

        <v-row>
            <v-col cols=12>
                <h2 class="subheading grey--text">Birthday</h2>

                <VueDatePicker 
                    ref="menu"
                    @onOpen="menu = true"
                    @onClose="menu = false"
                    
                    v-model="date"
                    format="YYYY-MM-DD"
                    name="Birthday"
                    
                    color=#9f4fff
                    
                    placeholder="Choose birthday"
                    no-header
                    fullscreen-mobile

                    :min-date="`${new Date().getFullYear()-100}`"
                    :max-date="new Date()"   
                    />

            </v-col>
        </v-row>

        <v-row>
            <v-col cols=12>
                <h2 class="subheading grey--text mb-5">Years of Education</h2>
                <NumberInputSpinner
                    v-model="api.edu"
                    :min="0"
                    :max="100"
                    :integerOnly="true"
                    :rules="[(v) => !!v || 'Please Select a Gender']"
                    required

                    outlined/>

            </v-col>
        </v-row>

        <v-row><v-col><v-btn class="primary" style="margin-top:3vmin" id="btn1" @click="info">Submit</v-btn></v-col></v-row>
        
    </v-container>

</div> 
</template>

<script lang="ts">
import { data } from "@/model/Data";
import Vue from "vue";
import NumberInputSpinner from "vue-number-input-spinner";

import {VueDatePicker} from "@mathieustan/vue-datepicker";
import "@mathieustan/vue-datepicker/dist/vue-datepicker.min.css";

export default Vue.extend({
    
    data: () => ({
        api: data,
        gender: {val: -1},
        edu: 0,
        details: 0,
        menu: false,
        date: null as unknown as string,
        activePicker: "YEAR",
    }),

    components: {NumberInputSpinner, VueDatePicker},

    watch: {
        menu(val) {
            val && setTimeout(() => (this.$refs.menu.$refs.agenda.mode = 'year'));
        }
    },

    methods: {

        info() {
            // Input validation (Add popup for this)
            if (this.gender.val == 0) return;
            if (this.date == null) return;

            // Retarded code to calculate age from bday
            var now = new Date();
            var bday = new Date(Date.parse(this.date));
            this.api.age = now.getFullYear() - bday.getFullYear();
            now.setFullYear(now.getFullYear() - this.api.age);
            if (now.valueOf() < bday.valueOf()) this.api.age -= 1;

            this.$emit("complete");
        }
    },
});
</script>