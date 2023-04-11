const Film = ({name, url}) => {
    return ( <>
        <li>
            <a href={url} target="_blank" rel="noreferrer">{name}</a>
        </li></>
     );
}
 
export default Film;