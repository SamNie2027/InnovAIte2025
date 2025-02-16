import * as Location from 'expo-location';
import { useState, useEffect } from 'react';

const useLocation = () => {
    const [errorMsg, setErrorMsg] = useState('');
    const [longitude, setLongitude] = useState(0);
    const [latitude, setLatitude] = useState(0);

    useEffect(() => {
        const getUserLocation = async () => {
            let { status } = await Location.requestForegroundPermissionsAsync();

            if (status !== 'granted') {
                setErrorMsg('Permission to use location was not granted');
                return;
            }

            let { coords } = await Location.getCurrentPositionAsync();

            if (coords) {
                setLatitude(coords.latitude);
                setLongitude(coords.longitude);
            }
        };

        getUserLocation();
    }, []); // Empty dependency array ensures this runs once when the component mounts

    return { latitude, longitude, errorMsg };
};

export default useLocation;
