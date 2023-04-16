import React, { useState, useEffect } from 'react';

import Fact from "../components/Fact";
import FactButton from "../components/FactButton";
import CocktailList from '../components/CocktailList';

const RandomContainer = () => {

    const [fact, setFact] = useState("")
    const [spirits, setSpirits] = useState([])

    useEffect(() => {
        fetchFact()
    }, [])

    useEffect(() => {
        fetchSpirits()
    }, [])

    const fetchFact = () => fetch("https://uselessfacts.jsph.pl/api/v2/facts/random").then(res => res.json()).then(data => setFact(data))
    const fetchSpirits = () => fetch("www.thecocktaildb.com/api/json/v1/1/list.php?c=list",  {headers: {
        'Accept': 'application/json'}}).then(res => console.log(res.json()).then(data => console.log(data.drinks)))

    const handleSelectedSpirit = chosenSpirit => setSpirits([...spirits, chosenSpirit])

    console.log(spirits)

    return ( 
        <>
            <h2>Tell me a...</h2>
            <FactButton fetchFact={fetchFact}/>
            <Fact fact={fact}/>
            <h2>Show me how to make cocktails with...</h2>
            <CocktailList spirits={spirits} handleSelectedSpirit={handleSelectedSpirit}/>
        </>
     );
}
 
export default RandomContainer;