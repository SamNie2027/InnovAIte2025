import { StyleSheet } from 'react-native';
import { Title } from './Title';
import { Description } from './Description';
import { ImageButton } from './ImageButton';

export const TattleTell = () => {
    return (
        <div style={styles.tattleTell}>
            <ImageButton/>
        </div>
    )
}

const styles = StyleSheet.create({
    tattleTell: {
        backgroundColor: '#79B791',
        paddingVertical: '10%'
    },
    title: {
        marginBottom: '10%'
    },
    description: {
        marginBottom: '20%'
    },
    imageButton: {
        marginTop: '20%'
    }
});