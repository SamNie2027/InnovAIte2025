import { StyleSheet, View } from "react-native";
import { Title } from "./Title";
import { Description } from "./Description";
import { ImageButton } from "./ImageButton";

export const TattleTell = () => {
  return (
    <View style={styles.container}>
      <View style={styles.tattleTell}>
        <Title />
        <Description />
        <ImageButton />
      </View>
    </View>
  );
};

export default TattleTell;

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  tattleTell: {
    alignItems: "center",
    justifyContent: "center",
  },
});
