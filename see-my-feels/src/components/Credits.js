import { FaGithub } from "@react-icons/all-files/fa/FaGithub";

export function Credits() {
    return(
        <div style={{paddingBottom:"2em"}}>
            <p style={{textAlign:"center"}}>Created by: Jules Dehon, Casey Williams, Alexandru Moraru</p>
            <a href="https://github.com/shnupta/SeeMyFeels">
                <FaGithub style={{width:"3em", height:"3em"}}/>
            </a> 
        </div>
    )
}