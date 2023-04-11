const ExternalLink = () => {
    const link = "https://www.imdb.com/calendar/?region=gb"
    return ( 
        <>
        <h3>
            <a href={link} target="_blank" rel="noreferrer">Click here for more</a>
        </h3>
        </>
     );
}
 
export default ExternalLink;