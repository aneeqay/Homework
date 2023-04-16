import Cocktail from "./Cocktail";
import Spirit from "./Spirit";

const CocktailList = ({spirits, handleSpirits}) => {

    if (spirits === []) return

    const mappedSpirit = spirits.map((spirit, index) => {
        return <Spirit
        key={index}
        spirit={spirit}>
        {spirit.strDrink}
        </Spirit>
    })

    const handleSelect = () => {

    }

    return ( 
        <>
            <select onChange={handleSelect}>CocktailList
                <option>{mappedSpirit}</option>
            </select>
        </>
     );
}
 
export default CocktailList;