const FactButton = ({fetchFact}) => {

    const handleClick = () => {
        fetchFact()
    }

    return ( 
        <>
            <button onClick={handleClick}>Random Fact</button>
        </>
     );
}
 
export default FactButton;
