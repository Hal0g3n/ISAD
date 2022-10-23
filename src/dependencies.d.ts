declare module "*.vue" {
  import Vue from "vue";
  export default Vue;
}

declare module "vuetify/lib/framework" {
    import Vuetify from "vuetify";
    export default Vuetify;
}

declare module "vue-step-progress-indicator" {
    import VueStepProgressIndicator from "vue-step-progress-indicator";
    export default VueStepProgressIndicator;
}

declare module "vue-ellipse-progress" {
    import { VueEllipseProgress } from "vue-ellipse-progress";
    export default VueEllipseProgress;
}

declare module "vue-number-input-spinner" {
    import NumberInputSpinner from "vue-number-input-spinner";
    export default NumberInputSpinner;
}

declare module "@mathieustan/vue-datepicker" {
    import VueDatePicker from "@mathieustan/vue-datepicker";
    export default VueDatePicker;
}